#include<stdio.h>
int main()
{
	int n,k,*a,i,q;
	a=(int*)malloc(n*sizeof(int));
	void rotation(int*,int,int);
	printf("enter the no of elements,no of rotations and the index\n");
	scanf("%d%d%d",&n,&k,&q);
	printf("enter the elements\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	rotation(a,k,n);
	printf("after rotating %d times\n",k);
	for(i=0;i<n;i++)
	{
		printf("%d",a[i]);
	}
	printf("the a[%d] element is %d\n",q,a[q]);
	return 0;

}
void rotation(int a[],int k,int n)
{
	int temp;
	if(k!=0)
	{
		temp=a[n-1];
		for(i=n-1;i>0;i--)
			a[i]=a[i-1];
		a[0]=temp;
		rotation(a,k-1,n);
	}
}