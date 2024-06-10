#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
struct _ListNode
{
    struct _ListNode *next;
    char *str;
};

typedef struct _ListNode ListNode;

ListNode *new_node(char *str);
void delete_node(ListNode *node);
ListNode *add_word(ListNode *node, char *str);
bool search_word(ListNode *node, char *str);
void show_list(ListNode *node);
void word_ai(char head, char *buf);
char last_char(char *str);

int main()
{
    int i;
    char outbuf[8];
    char inbuf[4];
    ListNode *head = NULL;

    printf("?aaaaaa\n"); fflush(stdout);
    while( 1 ) {
        scanf("%s", inbuf);

        if (inbuf[0] != 'a' || search_word(head, inbuf)) { break; }
        head = add_word(head, inbuf);
        
        word_ai(last_char(inbuf), outbuf);
        printf("?%s\n", outbuf); fflush(stdout);
    }
    printf ("!OUT\n");

    return 0;
}


ListNode * new_node(char *str)
{
    int len = strlen(str);
    ListNode *node = (ListNode *) malloc(sizeof(ListNode));
    node->next = NULL;
    node->str = (char *) malloc(sizeof(char) * (len + 1));
    strcpy(node->str, str);
    return node;
}

void delete_node(ListNode *node)
{
    free(node->str);
    free(node);
}

ListNode *add_word(ListNode *node, char *str)
{
    ListNode *newhead = new_node(str);
    newhead->next = node;
    return newhead;
}

bool search_word(ListNode *node, char *str)
{
    for(; node != NULL; node = node->next)
    {
        if (strcmp(str, node->str) == 0){
            return true;
        }
    }
    return false;
}

void show_list(ListNode *node)
{
    for(; node != NULL; node = node->next)
    {
        printf("%s\n", node->str);
    }
}

void word_ai(char head, char *buf)
{
    static int cnt = 0;
    buf[0] = head;
    buf[1] = 'a' + (cnt % 26);
    buf[2] = 'a' + (cnt / 26);
    buf[3] = 'a';
    buf[4] = '\0';
    cnt++;
}

char last_char(char *str)
{
    while (*(str + 1)) { str++; }
    return *str;
}