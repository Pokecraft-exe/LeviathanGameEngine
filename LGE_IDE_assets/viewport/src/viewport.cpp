#include <iostream>
#include <game.h>
#include <window.h>
#include <widgets.h>
using namespace std;

void drawXAxis(void* w, void* _this, int x, int y) {
	((window*)w)->drawLine(x, y, x + 100, y, 0x0000ff);
	((window*)w)->DrawRect(x + 100, y - 2, 2, 2, 0x0000ff);
}

void drawPickableWidget(void* w, void* _this, int x, int y);
int _onClick(void*) { return 0; }

class pickableWidget : public Button {
public:
	Scale Xaxis;
	Scale Yaxis;
	BaseWidget* wrapped;
	pickableWidget() {}
	pickableWidget(BaseWidget* w) {
		text = "";
		x = w->x;
		y = w->y;
		sizex = w->sizex;
		sizey = w->sizey;
		anchor = w->anchor;
		wrapped = w;
		ptrToWidget = this;
		Type = WIDGET_TYPE_CLICKABLE | WIDGET_TYPE_FOCUSABLE;
		draw = drawPickableWidget;
		OnClick = _onClick;

		Xaxis = Scale(sizex + x + 10, y, 100, 20, 100, true, nullptr);
		Yaxis = Scale(sizex / 2 + x, y - 110, 20, 100, 100, false, nullptr);
	}
	bool focused(window* w) {
		//cout << w->focused << " , " << ptrToWidget << endl;
		return (w->focused == ptrToWidget) ? true : false;
	}
};

void drawPickableWidget(void* w, void* _this, int x, int y) {
	((window*)w)->DrawRect(x, y, ((Entry*)_this)->sizex, ((Entry*)_this)->sizey, 0x0000ff);
	if (((pickableWidget*)_this)->focused((window*)w)) {
		cout << "a\n";//((pickableWidget*)_this)->Xaxis.attach(w);
		//((pickableWidget*)_this)->Yaxis.attach(w);
	}
}

int pickScreenAddLabel(void* _this);

class GameEngine : public SDLGameEngine {
public:
	window pickScreen;
	Button labelButton;
	Button button;
	pickableWidget pick;
	int widgetToAdd = 0;

	bool OnUserCreates() {
		pickScreen = window("Widgets", 250, 600);

		/*
		Label
		Image
		Button
		Entry
		CheckBox
		Scale

		customs.json
		*/

		labelButton = Button("Add Label", 1, 1, 100, 100, 0xffffff, pickScreenAddLabel, this);
		labelButton.ptrToWidget = &labelButton;
		labelButton.attach(&pickScreen);

		button = Button("Label", 1, 1, 100, 100, 0xffffff, pickScreenAddLabel, this);
		pick = pickableWidget(&labelButton);

		pick.attach(&pickScreen);
		button.attach(&pickScreen);
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) {
		screen.clear();
		pickScreen.clear();

		while (screen.PollEvent()) {
			if (screen.e.type == QUIT) quit = true;
		}
		while (pickScreen.PollEvent()) {
			if (pickScreen.e.type == QUIT) quit = true;
		}

		screen.DrawString("FPS: " + to_string(fps()), 10, 5, 0xff6666, 2);

		screen.DrawWidgets();
		pickScreen.DrawWidgets();

		screen.update();
		pickScreen.update();
		return true;
	}
};

int pickScreenAddLabel(void* _this) {
	((GameEngine*)_this)->labelButton.color = 0xff0000;
	return 0;
}

int main(int argc, char* args[])
{
	GameEngine game;

	game.CreateNewScreen("LGE 2D viewport", DEFAULT_WIDTH, DEFAULT_HEIGHT);

	game.start();

	return 0;
}