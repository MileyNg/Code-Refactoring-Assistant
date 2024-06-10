#include <stdio.h>
#include <stdlib.h>


typedef struct _queue_element queue_element;
struct _queue_element {
    void *value;
    queue_element *prev, *next;
};

typedef struct {
    int length;
    queue_element *first, *last;
} queue_t;


queue_t *queue_new() {
    queue_t *q;
    q = (queue_t*)malloc(sizeof(queue_t));
    q->length = 0;
    q->first = NULL;
    q->last = NULL;
    return q;
}

queue_element *queue_new_element(void *v) {
    queue_element *elm = (queue_element*)malloc(sizeof(queue_element));
    elm->value = v;
    elm->prev = elm->next = NULL;
    return elm;
}

void queue_delete(queue_t *q) {
    free(q);
}

queue_element *queue_get(queue_t *q, int n) {
    int i;
    queue_element *elm;
    if (n < 0 || q->length <= n) return NULL;
    elm = q->first;
    while (n--) {
        elm = elm->next;
    }
    return elm;
}

void *queue_pop(queue_t *q, int n) {
    queue_element *elm = queue_get(q, n);
    void *v;
    if (elm == NULL) { // pop last element
        elm = q->last;
        q->last = elm->prev;
        if (q->last == NULL) {
            q->first = NULL;
        }
        else {
            q->last->next = NULL;
        }
    }
    else {
        queue_element *ep, *en;
        ep = elm->prev;
        en = elm->next;
        if (ep != NULL) ep->next = en;
        if (en != NULL) en->prev = ep;
        if (elm == q->first) q->first = en;
        if (elm == q->last) q->last = ep;
    }
    v = elm->value;
    free(elm);
    q->length--;
    return v;
}

void queue_push(queue_t *q, void *v) {
    queue_element *elm = queue_new_element(v);
    if (q->last == NULL) {
        q->first = q->last = elm;
    }
    else {
        q->last->next = elm;
        elm->prev = q->last;
        q->last = elm;
    }
    q->length++;
}

void print_queue(queue_t *q, void (*print_elm)(void*)) {
    queue_element *elm = q->first;
    printf("Q(%d):", q->length);
    while (elm != NULL) {
        printf(" ");
        print_elm(elm->value);
        elm = elm->next;
    }
    printf("\n");
}


typedef struct {
    int width;
    int depth;
    int area;
} cake_t;


int cmp_int(const void *a, const void *b) {
    if (*(int *)a < *(int *)b) {
        return -1;
    }
    else if (*(int *)a == *(int *)b) {
        return 0;
    }
    return 1;
}

void print_cake(void *v) {
    cake_t *c = (cake_t*)v;
    printf("(%d, %d)", c->width, c->depth);
}


int main(void) {
    int n, w, d;
    cake_t cake[201];

    while (scanf("%d%d%d\n", &n, &w, &d) != EOF && (n || w || d)) {
        int area[101] = {};
        int i, ci = 0;
        queue_t *q = queue_new();
        cake_t *c = &cake[ci++];
        c->width = w;
        c->depth = d;
        c->area = w * d;
        queue_push(q, (void*)c);
        for (i = 0; i < n; i++) {
            int p, s, l;
            cake_t *c1, *c2;
            scanf("%d%d\n", &p, &s);

            c = (cake_t*)queue_pop(q, p-1);
            s = s % (c->width + c->depth);
            c1 = &cake[ci++];
            c2 = &cake[ci++];
            if (s < c->width) {
                c1->depth = c2->depth = c->depth;
                l = c->width - s;
                if (s < l) {
                    c1->width = s;
                    c2->width = l;
                }
                else {
                    c1->width = l;
                    c2->width = s;
                }
            }
            else {
                c1->width = c2->width = c->width;
                s = s - c->width;
                l = c->depth - s;
                if (s < l) {
                    c1->depth = s;
                    c2->depth = l;
                }
                else {
                    c1->depth = l;
                    c2->depth = s;
                }
            }
            c1->area = c1->width * c1->depth;
            c2->area = c2->width * c2->depth;
            
            queue_push(q, (void*)c1);
            queue_push(q, (void*)c2);
            // print_queue(q, print_cake);
        }
        
        for (i = 0; i < q->length; i++) {
            c = (cake_t*)(queue_get(q, i)->value);
            area[i] = c->area;
        }
        
        qsort(area, q->length, sizeof(int), cmp_int);
        printf("%d", area[0]);
        for (i = 1; i < q->length; i++) {
            printf(" %d", area[i]);
        }
        printf("\n");

        queue_delete(q);
    }
    return 0;
}