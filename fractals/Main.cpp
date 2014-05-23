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

class Pixel {
 public:
  Pixel(complex<float> c, int i, int j);
  complex<float> c, d;
  float r, g, b;
  int iter, i, j; //i, j screen coords location
  void iterate();
  void draw();
  void update(complex<float> c);
};

Pixel::Pixel(complex<float> c, int i, int j) {
  d = complex<float> (0, 0);
  iter = 0;
  this->i = i;
  this->j = j;
  this->c = c;
  r = g = b = 0.0f;
}

void Pixel::update(complex<float> c) { 
  this->c = c; 
  d = complex<float> (0, 0);
  this->iter = 0; 
  r = g = b = 0.0f;
}

/* Vars */
Viewport viewport;
float minx = -2, maxx = 1, miny = -1, maxy = 1;
vector<Pixel> pixels;
int max_iter = 100;
float remap(float v, float froml, float fromh, float tol, float toh) {
  return ((v-froml) * (toh - tol))/(fromh - froml) + tol; }

void myReshape(int w, int h) {
  viewport.w = w;
  viewport.h = h;

  glViewport (0, 0, viewport.w, viewport.h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(0, viewport.w, 0, viewport.h);
}

void Pixel::draw() {
  glColor3f(r, g, b);
  glVertex2f(i + 0.5, j + 0.5);
}

void update_pixel_locations() {
  for (Pixel& p : pixels) {
    p.update(complex<float>(remap(p.i, 0, viewport.w, minx, maxx), remap(p.j, 0, viewport.h, miny, maxy)));
  }
}

void initScene() {
  myReshape(viewport.w,viewport.h);
  glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
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

void Pixel::iterate() {
  while (norm(d) < 4.0f && iter++ < max_iter) {
    d = d*d + c;
  }
  HSVtoRGB(iter * (360.0f/max_iter), 1, 1, r, g, b); 
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
  glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

  glBegin(GL_POINTS);

  for (Pixel p : pixels) {
    p.iterate();
    p.draw();
  }

  glEnd();
  glutSwapBuffers();
}

void mySpecial(int key, int xx, int yy) {
  switch (key) {
    case GLUT_KEY_LEFT:
      minx -= 0.1*(maxx-minx);
      maxx -= 0.1*(maxx-minx);
      break;
    case GLUT_KEY_RIGHT:
      minx += 0.15*(maxx-minx);
      maxx += 0.15*(maxx-minx);
      break;
    case GLUT_KEY_UP:
      miny += 0.1*(maxy-miny);
      maxy += 0.1*(maxy-miny);
      break;
    case GLUT_KEY_DOWN:
      miny -= 0.1*(maxy-miny);
      maxy -= 0.1*(maxy-miny);
      break;
    default:
      break;
  }
  cout << "Shifted: " << minx << ' ' << maxx << ' ' << miny << ' ' << maxy << endl;
}

void myKeyboard(unsigned char key, int xx, int yy) { 
  switch (key) {
  case 13: //Enter, quit
    exit(0);
    break;
  case 'i':
    /* Another iteration */
    max_iter += 5;
    cout << "Max iterations is now " << max_iter << endl;
    break;
  case 'u':
    max_iter -= 5;
    cout << "Max iterations is now " << max_iter << endl;
    break;
  case '=':
    //minx += 0.15;
    //maxx -= 0.15;
    //miny += 0.1;
    //maxy -= 0.1;
    minx *= 0.7;
    maxx *= 0.7;
    miny *= 0.7;
    maxy *= 0.7;
    cout << "Zooming in: " << minx << ' ' << maxx << ' ' << miny << ' ' << maxy << endl;
    break;
  case '-':
    //minx -= 0.15;
    //maxx += 0.15;
    //miny -= 0.1;
    //maxy += 0.1;
    minx *= 1.3;
    maxx *= 1.3;
    miny *= 1.3;
    maxy *= 1.3;
    cout << "Zooming out: " << minx << ' ' << maxx << ' ' << miny << ' ' << maxy << endl;
    break;
  case 'r':
    cout << "Redrawing... " << endl;
    update_pixel_locations();
    glutPostRedisplay();
    break;
  default:
    break;
  }
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

  for (int i = 0; i < viewport.w; ++i) {
    for (int j = 0; j < viewport.h; ++j) {
      pixels.emplace_back(complex<float>(remap(i, 0, viewport.w, minx, maxx), remap(j, 0, viewport.h, miny, maxy)), i, j);
    }
  }

  glutDisplayFunc(myDisplay);
  glutReshapeFunc(myReshape);
  glutKeyboardFunc(myKeyboard);
  glutSpecialFunc(mySpecial);
  glutMainLoop();  

  return 0;
}

