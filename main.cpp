#include <iostream>
#include <stdio.h>
#include <vector>

void print_board(std::vector<char> &board)
{
    printf("1   3\n");
    printf("%c|%c|%c\n", board[0], board[1], board[2]);
    printf("%c|%c|%c\n", board[3], board[4], board[5]);
    printf("%c|%c|%c\n", board[6], board[7], board[8]);
    printf("7   9\n");
}

void initialize_board(std::vector<char> &board)
{
    for (int i = 0; i < 9; i++)
    {
        board.push_back(' ');
    }
}

int state_check(std::vector<char> &board)
{

    // horizontal checks
    if ((board[0] == board[1] && board[1] == board[2]) && board[0] != ' ' ||
        (board[3] == board[4] && board[4] == board[5]) && board[3] != ' ' ||
        (board[6] == board[7] && board[7] == board[8]) && board[6] != ' ')
    {
        return 1;
    }
    // vertical checks
    if ((board[0] == board[3] && board[3] == board[6]) && board[0] != ' ' ||
        (board[1] == board[4] && board[4] == board[7]) && board[1] != ' ' ||
        (board[2] == board[5] && board[5] == board[8]) && board[2] != ' ')
    {
        return 1;
    }

    // diagonal checks
    if ((board[0] == board[4] && board[4] == board[8]) && board[0] != ' ' ||
        (board[6] == board[4] && board[4] == board[2]) && board[6] != ' ')
    {
        return 1;
    }
    bool draw = true;

    for (char v : board)
    {
        if (v == ' ')
            draw = false;
    }

    if (draw)
        return 2;

    return 0;
}

int main()
{

    std::vector<char> board;
    initialize_board(board);

    int mv;
    bool play = true;
    int turn = 0;
    int state = 0;

    while (play)
    {
        print_board(board);
        state = state_check(board);

        if (state == 1)
        {
            turn ^= 1;
            printf("Player %d (%c) won\n", turn + 1, turn ? 'X' : 'O');
            play = false;
            continue;
        }
        else if (state == 2)
        {
            std::cout << "DRAW NIGGA\n";
            play = false;
            continue;
        }

        printf("player %d (%c) > ", turn + 1, turn ? 'X' : 'O');
        std::cin >> mv;
        mv -= 1;

        if ((mv < 0 || mv > 8) || board[mv] != ' ')
        {
            std::cout << "tf nigga\n";
            std::cin.clear();
            std::cin.ignore();
        }
        else
        {
            board[mv] = turn ? 'X' : 'O';
            turn ^= 1;
        }
    }
}