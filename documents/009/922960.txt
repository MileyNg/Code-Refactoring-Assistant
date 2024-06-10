#include <iostream>


using namespace std;


int main(){
	int rooms[4][3][10] = { 0 };

	int n;

	cin >> n;

	int b, f, r, v;

	for (int i = 0; i < n; i++){
		cin >> b >> f >> r >> v;
		rooms[b-1][f-1][r-1] = rooms[b-1][f-1][r-1]+v;
	}
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 3; j++){
			cout << " ";
			for (int k = 0; k < 10; k++){
				cout << rooms[i][j][k];
				if (k != 9) cout << " ";
			}
			cout << endl;
		}
		if (i != 3) cout << "####################" << endl;
	}
	return 0;
}