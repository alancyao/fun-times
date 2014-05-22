#include <string>
#include <complex>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <memory>
#include <GL/glut.h>
#include <GL/glu.h>
#include <stdio.h>
#include <SOIL/SOIL.h>

using namespace std;

class Viewport {
  public:
    int w, h; // width and height
};

/* Statics */
Viewport viewport;
float minx = -2, maxx = 1, miny = -1, maxy = 1;

void myReshape(int w, int h) {
  viewport.w = w;
  viewport.h = h;

  glViewport (0, 0, viewport.w, viewport.h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0, viewport.w, 0, viewport.h);
}

void initScene() {
  glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
  myReshape(viewport.w,viewport.h);
}

void setPixel(int x, int y, GLfloat r, GLfloat g, GLfloat b) {
  glColor3f(r, g, b);
  glVertex2f(x + 0.5, y + 0.5);
}

void HSVtoRGB(int h, float s, float v, float& r, float& g, float& b) {
  /* h \in [0, 360] */
  float c = v*s;
  float hscale = h/60.0f;
  float x = c*(1-abs(fmod(hscale, 2) - 1));
  r = g = b = 0;
  if ((0 <= hscale) && (hscale < 1)) {
    r = c; g = x;
  } else if ((1 <= hscale) && (hscale < 2)) {
    r = x; g = c;
  } else if ((2 <= hscale) && (hscale < 3)) {
    g = c; b = x;
  } else if ((3 <= hscale) && (hscale < 4)) {
    g = x; b = g;
  } else if ((4 <= hscale) && (hscale < 5)) {
    r = x; b = c;
  } else if ((5 <= hscale) && (hscale < 6)) {
    /* special */
    //r = c; b = x;
    r = x; b = x;
  }
  float m = v - c;
  r += m; g += m; b += m;
}

void inSet(complex<float> c, float& r, float& g, float& b) {
  complex<float> d {0.0, 0.0};
  int iter = 0, max_iter = 300;
  while (norm(d) < 4.0f && iter++ < max_iter) {
    d = d*d + c;
  }
  HSVtoRGB(iter * (360.0f/max_iter), 1, 1, r, g, b); 
}

float remap(float v, float froml, float fromh, float tol, float toh) {
  return ((v-froml) * (toh - tol))/(fromh - froml) + tol;
}

void myDisplay() {
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glEnable(GL_DEPTH_TEST);
  glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);
  glEnable(GL_COLOR_MATERIAL);

  /* Set up camera */
  glViewport (0, 0, viewport.w, viewport.h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0, viewport.w, 0, viewport.h);
  glClear(GL_COLOR_BUFFER_BIT);

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();

  glBegin(GL_POINTS);

  float r, g, b;
  for (auto i = 0; i < viewport.w; ++i) {
    for (auto j = 0; j < viewport.h; ++j) {
      inSet(complex<float>(remap(i, 0, viewport.w, minx, maxx), remap(j, 0, viewport.h, miny, maxy)), r, g, b);
      setPixel(i, j, r, g, b);
    }
  }

  glEnd();
  glutSwapBuffers();
}

void myKeyboard(unsigned char key, int xx, int yy) { 
  switch (key) {
  case 13: //Enter, quit
    exit(0);
    break;
  case 'i':
    /* Another iteration */
    glutPostRedisplay();
    break;
  case '=':
    break;
  case '-':
    break;
  default:
    break;
  }
  glutPostRedisplay();
}

int main(int argc, char *argv[]) {
  glutInit(&argc, argv);
  
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );
  viewport.w = 720;
  viewport.h = 480;
  glutInitWindowSize(viewport.w, viewport.h);
  glutInitWindowPosition(0, 0);
  glutCreateWindow(argv[0]);
  initScene();

  glutDisplayFunc(myDisplay);
  glutReshapeFunc(myReshape);
  glutKeyboardFunc(myKeyboard);
  glutMainLoop();  

  return 0;
}

