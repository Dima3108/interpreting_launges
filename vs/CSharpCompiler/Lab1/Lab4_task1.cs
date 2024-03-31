using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab4_task1
    {
        public static uint CostCalculation(int[] AmountOfGarbage,int offset)
        {
            int a=offset-1; int b=offset+1;
            bool[]stat=new bool[AmountOfGarbage.Length];
            stat[offset] = true;
            int tot_count = 1;
            int price_a = 1, price_b = 1;
            uint total_sum = 0;
            while(tot_count<AmountOfGarbage.Length)
            {
                if (a < 0)
                {
                    a = AmountOfGarbage.Length - 1;
                }
                if (b >= AmountOfGarbage.Length)
                {
                    b = 0;
                }
                if (stat[a] == false)
                {
                    stat[a] = true;
                    total_sum = (uint)(price_a * AmountOfGarbage[a]);
                    tot_count++;
                    
                }
                if ( stat[b] == false)
                {
                    stat[b] = true;
                    total_sum = (uint)(price_b * AmountOfGarbage[b]);
                    tot_count++;
                    
                }
                
                a--;
                b++;
                price_a++;
                price_b++;
            }
           
            return total_sum;
        }
        public static int GetIndex(int[] AmountOfGarbage)
        {
            int ind = 0;
            uint tsum=CostCalculation(AmountOfGarbage,0);
            uint ctsum = tsum;
            //for(int i = 1; i < AmountOfGarbage.Length; i++)
            uint[]cesh_sum=new uint[AmountOfGarbage.Length];
            Parallel.For(0, AmountOfGarbage.Length, i =>
            {
                cesh_sum[i] = CostCalculation(AmountOfGarbage, i);
            });
            for(int i = 1; i < AmountOfGarbage.Length; i++)
            {
                if (cesh_sum[i] < tsum)
                {
                    tsum = cesh_sum[i];
                    ind = i;
                }
            }
            return ind;
        }
    }
}
