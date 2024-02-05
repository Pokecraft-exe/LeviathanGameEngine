#include <iostream>
#include <game.h>
#include <window.h>
#include <widgets.h>
using namespace std;

void drawXAxis(void* w, void* _this, int x, int y) {
	((window*)w)->drawLine(x, y, x + 100, y, 0x0000ff);
	((window*)w)->DrawRect(x + 100, y - 2, 2, 2, 0x0000ff);
}

class pickableLabel : Button {
	Scale Xaxis = Scale();
	Scale  Yaxis = Scale();
	pickableLabel() {
		text = "Label";
		x = 0;
		y = 0;
		anchor = ANCHOR::NORTH_EAST;
		ptrToWidget = this;
		Type = WIDGET_TYPE_FOCUSABLE;
	}
}

int pickScreenAddLabel(void* _this);

class GameEngine : public SDLGameEngine {
public:
	window pickScreen;
	Button labelButton;
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
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) {
		screen.fill(0x00FFFF);
		pickScreen.clear();

		screen.PollEvent();
		pickScreen.PollEvent();

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