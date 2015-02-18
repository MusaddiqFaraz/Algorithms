#include<stdio.h>
#include<stdlib.h>
#define Max 100
int main()
{
	
	int a[Max],i,n;
	void Shellsort(int*,int);
	printf("enter the number of elements\n");
	scanf("%d",&n);
	printf("enter the elements to be sorted\n");
	for(i=1;i<=n;i++)
	{
		scanf("%d",&a[i]);
	}
	Shellsort(a,n);
	printf("the sorted elements are\n");
	for(i=1;i<=n;i++)
	{
		printf("%d\t",a[i]);
	}printf("\n");
}
void Shellsort(int a[],int n)
{
	int i,j,h=4,v;
	
	while(h>0)
	{
		
		for(i=1;i<=n;i++)
		{
			v=a[i];
			j=i;
			while(a[j-h]>v && j>=h)
			{
				a[j]=a[j-h];
				j=j-h;
			}
			a[j]=v;
			
		}
		if (h/2 != 0)
     		 h = h/2;
   		else if (h == 1)
    		  h = 0;
    	else
     		 h = 1;
	}
}