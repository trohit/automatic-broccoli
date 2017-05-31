/*
 * Program to find kth max element.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
int parent(int x) { return (x-1)/2; }
int lchild(int n) { return (2*n) + 1;}
int rchild(int n) { return (2*n) + 2;}
void displevel(int *arr, int len)
{
    printf("\n");
    for(int i = 0; i < len; i++) {
        printf("[%u]", arr[i]);
    }
}

void swap(int *a, int *b, bool is_special)
{
    if (is_special) {
        printf("is_special: %u swap %u<>%u", is_special, *a, *b);
    } else {
        printf("NOT_special: %u swap %u<>%u", is_special, *a, *b);
    }
    assert(*a !=*b);
    int t = *a;
    *a = *b;
    *b = t;
}
void heapify(int *arr, int pos, int len)
{
    static int cc = 0;
    cc++;
    int maxpos;
    int lpos = lchild(pos);
    int rpos = rchild(pos);

    int l = arr[lpos];
    int r = arr[rpos];
    int c = arr[pos];
    maxpos = pos;
    printf("\n%s: pos:%u %u @%u", __FUNCTION__, pos, arr[pos], len);
    if (pos >=0 ) {
        if (lpos < len && l > arr[maxpos]) {
            maxpos = lpos;
            printf("maxpos:l pos(%u:%u:%u) %u:%u:%u", lpos, pos, rpos, l, c, r);
        }
        if (rpos < len && r > arr[maxpos]) {
            maxpos = rpos;
            printf("maxpos:r pos(%u:%u:%u) %u:%u:%u", lpos, pos, rpos, l, c, r);
        }
        if (pos != maxpos) {
            swap(&arr[maxpos], &arr[pos], 0);
            displevel(arr, len);
            heapify(arr, maxpos, len);
        }
        //displevel(arr, len);
    }
}
/*
            50
           /  \
         40   30
        /  \     \
       10  20
 */
void buildheap(int arr[], int len)
{
    int i;
    for(i=len/2; i>=0;i--) {
        heapify(arr, i, len);
    }
}
int extract_max(int *arr, int len)
{
    if (len == 0) {
        return -1;
    }
    if (len == 1) {
        printf("\n >>> extract_max: last_elm:%u\n", arr[0]);
        return arr[0];
    }
    //displevel(arr, len);
    swap(&arr[0], &arr[len-1], 1);
    heapify(arr, 0, len-1);
    displevel(arr, len);
    printf("<- PICK");
    printf("\n  >>> extract_max: len:%u max:%u\n", len, arr[len-1]);
    return arr[len-1];
}
int findkmax(int arr[], int len, int k)
{
    int i = 1;
    int max = 0;
    buildheap(arr, len);
    printf("\n----Heap built----");
    displevel(arr, len);
    while (len >= 0) {
        max = extract_max(arr, len--);
        if (i == k) {
            printf("%s: returning [%u]", __FUNCTION__, max);
            return max;
        }
        i++;
    }
    assert(false);
}
int main()
{
    int arr[] = {10, 20, 30, 40, 50, 60, 70};
    int len = sizeof(arr) / sizeof(arr[0]);
    //findkmax(arr, len, 2);
    //displevel(arr, len);
    printf("\n <<<<>>>>>>Kth max is [%u]", findkmax(arr, len, 7));
    return 0;
}
