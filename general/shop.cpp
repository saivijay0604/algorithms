#include<iostream>
using namespace std;
float bread=2.25, milk=3.5, egg=1.75;

int main()
{
	int quantityOfBread = 20;
	int quantityOfMilk = 30;
	int quantityOfEgg = 25; 
	cout << "cost of single bread : $"<< bread <<endl;
	cout << "cost of single milk can : $"<< milk <<endl;
	cout << "cost of single egg : $"<< egg <<endl;
	cout << "____________________________________________" <<endl ;
	cout << "____________________________________________" <<endl ;
	
	int NoOfBread, NoOfMilk, NoOfEgg;
	int calculateNoOfBread = 0;
	int calculateNoOfMilk = 0;
	int calculateNoOfEgg = 0;
	float sum;
	do
	{
		cout << "********************************************" << endl;
		//BREAD
		cout <<"No of breads : ";
		cin >> NoOfBread ;
		if(!(NoOfBread <= quantityOfBread - calculateNoOfBread ))
		{
			quantityOfBread = quantityOfBread - calculateNoOfBread;
			if ((quantityOfBread > 0))	
			{ 
				do
				{
				cout << "we have only " << quantityOfBread << " Bread's" <<endl;
				cout <<"No of breads : ";
				cin >> NoOfBread ;			
				}while ((NoOfBread > quantityOfBread) && ((quantityOfBread >= 0)));
			}
			else
			{
				cout << "sorry sir ,out of stock" << endl;	
			}
		}	
		
		//MILK
		cout << "No of milks :";
		cin >> NoOfMilk;
		if(NoOfMilk > quantityOfMilk - calculateNoOfMilk)
		{
			quantityOfMilk = quantityOfMilk - calculateNoOfMilk;
			if ((quantityOfMilk > 0))	
			{ 
				do
				{
					cout << "we have only " << quantityOfMilk<< " Milk's" <<endl;
					cout << "No of milks :";
					cin >> NoOfMilk;	
				}while ((NoOfMilk > quantityOfMilk) && ( quantityOfMilk >= 0) );
			}
			else
			{
				cout << "sorry sir ,out of stock" << endl;	
			}
			
		}
		//EGGS
		cout << "No of eggs : ";
		cin  >> NoOfEgg;
		if(NoOfEgg > quantityOfEgg - calculateNoOfEgg)	
		{	
			quantityOfEgg = quantityOfEgg - calculateNoOfEgg;
			if((quantityOfEgg > 0))
			{
				do
				{
					cout << "we have only " << quantityOfEgg << " Egg's" <<endl;
					cout << "No of eggs : ";
					cin  >> NoOfEgg;
				}while ((NoOfEgg > quantityOfEgg) && (quantityOfEgg >= 0));
			}
			else
			{
				cout << "sorry sir ,out of stock" << endl;	
			}
		}
		
		sum = NoOfBread*bread + NoOfMilk*milk + NoOfEgg*egg;
		cout << "Total cost : " <<sum <<endl<<endl;
		
		if(sum !=0)
		{
			string payment;
			cout << "payment through cash or card :" ;
			cin >>payment;
			
			if(payment == "card" && payment =="CARD")
			{
				cout << "Thank You" <<endl ;
				cout  << "________________________________________________________________" << endl;
			}
			else if(payment == "cash" || payment == "CASH" )
			{
				float customerAmount;
				float returnAmount;
				returnAmount = sum;
				do
				{
					cout << "Enter the amount  by customer :";
					cin >> customerAmount ;
			 		returnAmount = returnAmount-customerAmount;
			 		if(returnAmount > 0)
			 		{
			 			cout << "customer still need  to pay :" << returnAmount << endl;
					}
					
				}while(returnAmount > 0);
				
				if(returnAmount <= 0)
				{
					returnAmount = (-returnAmount);
					cout << "Return amount to customer : " << returnAmount << endl;
				}
				cout << "Thank You"<<endl ;
				cout  << "________________________________________________________________" << endl;
			}
		}	
		calculateNoOfBread = calculateNoOfBread + NoOfBread;
		calculateNoOfMilk = calculateNoOfMilk + NoOfMilk;
		calculateNoOfEgg = calculateNoOfEgg + NoOfEgg;		
	}while(sum!=0);
	
	cout << "Number of Bread sold in a day : " << calculateNoOfBread << endl;
	cout << "Number of Milk sold in a day : " << calculateNoOfMilk << endl;
	cout << "Number of Egg sold in a day : " << calculateNoOfEgg << endl;
}
