using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab1_task5
    {
        public static int[] array_ = new int[1024];
        private static int[] GetRandomArray()
        {
            int[]array=new int[1024];
            Random random = new Random();
            for(int i=0;i<array.Length;i++)
                array[i] = random.Next(0,256);
            return array;
        }
        private static void print_array(int[] array)
        {
            for(int i = 0; i < array.Length ; i++)
            {
                Console.Write(array[i].ToString()+" ");
                if((i+1)%32==0)
                    Console.WriteLine();
            }
        }
    }
}
