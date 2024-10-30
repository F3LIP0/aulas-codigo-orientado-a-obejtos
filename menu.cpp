#include <iostream>
using namespace std;
int main(){
    int opcao;
    do {
        cout << "Menu" << endl;
        cout << "1. exibir mensagem 1" << endl;
        cout << "2. exibir mensagem 2" << endl;
        cout << "3. sair" << endl;
        cout << "\n" << endl;
        cout << "Escolha uma opção: ";
        cin >> opcao;

        if (opcao == 1) {
            cout << "\n";
            cout << "MENSAGEM 1";
            cout << "\n";
            opcao = 3;
        } else if (opcao == 2) {
            cout << "\n";
            cout << "MENSAGEM 2";
            cout << "\n";
            opcao = 3;
        }

    } while (opcao != 3);
    cout << "Saindo do programa. " << endl;
}