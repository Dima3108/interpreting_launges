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
        /*В порядке увеличения квадратичного отклонения между наибольшим 
          ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально 
          расположенных символов строки (относительно ее середины)*/
        public static string[] task_9(string[] array)
        {
            var delt=new double[array.Length];
            for(int i = 0; i < array.Length; i++)
            {
                string s = array[i];
                char c = s[0];//максимальный символ
                for (int j = 0; j < s.Length; j++)
                    if (c < s[j])
                        c = s[j];
                int ser1 = s.Length / 2;
                int ser2 = ser1;
                if(s.Length % 2 == 0)
                {
                    ser2 = ser1 - 1;
                }
                int delta = s[ser2] - s[ser1];
                while (ser2 >= 0 && ser1 < s.Length)
                {
                    delta += s[ser2] - s[ser1];
                    ser2--;
                    ser1++;
                }
                int max_ch = c;
                delt[i]=(double)((delta-max_ch)*(delta-max_ch));
            }
            string[]s2=new string[array.Length];    
            for(int k=0;k< array.Length;k++)
                s2[k] = array[k];
            for(int i = 0; i < array.Length; i++)
            {
                double tmpd = delt[i];
                string tmpv = "";
                for(int j = i + 1; j < array.Length; j++)
                {
                    if (tmpd > delt[j])
                    {
                        delt[i] = delt[j];
                        delt[j] = tmpd;
                        tmpd = delt[i];
                        tmpv = s2[i];
                        s2[i] = s2[j];
                        s2[j] = tmpv;
                    }
                }
            }
            return s2;
        }
    }
}
