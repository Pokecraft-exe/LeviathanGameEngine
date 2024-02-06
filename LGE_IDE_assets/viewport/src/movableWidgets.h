#pragma once
#include <widgets.h>
using std::string;

class MovableLabel : public BaseWidget {
public:
	MovableLabel() {}
	MovableLabel(string text, Color color, int x, int y);
	string text;
	Color color;
};

class MovableImage : public BaseWidget {
public:
	MovableLabel() {}
	MovableLabel(string image, int x, int y);
	SDL_Surface* image;
};



typedef int FUNCTION_CALL(void*);

class MovableButton : public BaseWidget {
public:
	MovableButton() {}
	MovableButton(string text, int x, int y, int sizex, int sizey, Color color, FUNCTION_CALL* OnClick, void* ptr);
	string text;
	Color color;
	FUNCTION_CALL* OnClick;
	void* ptr;
};



class MovableEntry : public BaseWidget {
public:
	MovableEntry() {}
	MovableEntry(string placeHolder, int x, int y, int sizex, int sizey);
	string value, placeHolder;
};



class MovableCheckBox : public Button {
public:
	MovableCheckBox() {}
	MovableCheckBox(string text, int x, int y);
	bool checked = false;
};



typedef int DRAG_CALL(void*, int, int);

void defaultOnDrag(void*, int, int);

class MovableScale : public BaseWidget {
public:
	MovableScale() {};
	MovableScale(int x, int y, int sizex, int sizey, int max, bool horizontal = true, DRAG_CALL* onDrag = nullptr);
	bool horizontal;
	DRAG_CALL* Drag;
	DRAG_CALL* OnDrag = nullptr;
	void* ptr;
	float value = 0;
	int max = 100;
};+