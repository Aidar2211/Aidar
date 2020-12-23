# include <stdio.h>
# include <stdlib.h>

struct
aeroflot
{
    char
nazn[12];
int
numr;
int
tip;
};

int
main()
{
    struct
aeroflot * airport;
int
n;
int
i;
int
tip;

n = 7;
airport = (struct aeroflot *)
malloc(n * sizeof(struct
aeroflot));

scanf("%d", & tip);

for (i=0;i < n;i++)
{
    scanf("%s", & airport[i].nazn);
scanf("%d", & airport[i].numr);
scanf("%d", & airport[i].tip);
}

for (i=0;i < n;i++)
{
printf("%d ", i);
printf("%s ", airport[i].nazn);
printf("%d ", airport[i].numr);
printf("%d", airport[i].tip);
printf("\n");
}

printf("\n");

for (i=0;i < n;i++)
{
if (airport[i].tip == tip)
{
printf("%d ", i);
printf("%s ", airport[i].nazn);
printf("%d ", airport[i].numr);
printf("%d", airport[i].tip);
printf("\n");
}

}

}