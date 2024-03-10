using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab1_task4
    {
        //10. В порядке увеличения среднего количества «зеркальных» троек 
        // (например, «ada») символов в строке
        /*
         * public static string[] task_10(string[] array)
         {
             int[]count=new int[array.Length];
             for(int i = 0; i < array.Length; i++)
             {
                 count[i] = 0;
                 for(int j = 0; j < array[i].Length - 2; j++)
                 {
                     if (array[i][j] == array[i][j + 2])
                         count[i]++;
                 }
             }
             string[]s2=new string[count.Length];    
             for(int i=0;i<count.Length;i++)
             {
                 s2[i] = array[i];
             }
             for(int i = 0; i < s2.Length; i++)
             {
                 var tmp_del = count[i];
                 for(int j = i + 1; j < s2.Length; j++)
                 {
                     if (tmp_del > count[j])
                     {
                         count[i] = count[j];
                         count[j] = tmp_del;
                         tmp_del = count[i];
                         var tmp_val = s2[i];
                         s2[i] = s2[j];
                         s2[j] = tmp_val;
                     }
                 }
             }
             return s2;  
         }
         */
        public static string[] task_10(string[] array)
        {
            int[]count=new int[array.Length];
            for(int i = 0; i < array.Length; i++)
            {
                count[i] = 0;
                for(int j = 0; j < array[i].Length - 2; j++)
                {
                    if (array[i][j] == array[i][j + 2])
                        count[i]++;
                }
            }
            string[]s2=new string[count.Length];    
            for(int i=0;i<count.Length;i++)
            {
                s2[i] = array[i];
            }
            for(int i = 0; i < s2.Length; i++)
            {
                var tmp_del = count[i];
                for(int j = i + 1; j < s2.Length; j++)
                {
                    if (tmp_del > count[j])
                    {
                        count[i] = count[j];
                        count[j] = tmp_del;
                        tmp_del = count[i];
                        var tmp_val = s2[i];
                        s2[i] = s2[j];
                        s2[j] = tmp_val;
                    }
                }
            }
            return s2;  
        }
    }
}
