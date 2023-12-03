#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main() {
  string nom_fichier;
  cout << "Enter the file name: ";
  cin >> nom_fichier;

  fstream monfichier, in;
  monfichier.open(nom_fichier,ios::in);
  
  string ligne,c;
  int i, j;
  char a,b;
  int nb_cara,coord;
  int somme=0;
  while(getline(monfichier, ligne)) //Tant qu'on n'est pas à la fin, on lit
  {
    nb_cara = ligne.size();
    i = 0;
    j = nb_cara - 1;

    while (i <= nb_cara-1) {
      if (isdigit(ligne[i])) {
        a = ligne[i];
        break;
      }
      i += 1;
    }

    while (j >= 0) {
      if (isdigit(ligne[j])) {
        b = ligne[j];
        break;
      }
      j -= 1;
    }
    c={a, b}; // concatenation de 2 char
    coord=stoi(c); // string to int
    cout << "la coord est : " << coord << endl;
    somme+=coord;
  }
  cout << "la somme est : " << somme << endl;
  return 0;
}
