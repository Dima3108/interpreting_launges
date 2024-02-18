using System;
using System.Runtime;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
namespace ForPython
{
    
    public class HelpFunctions
    {
        public static string[] TextInformation = { "Выберите задачу, которую хотите решить\n",//0
                                                  "у задачи ",                                //1
                                                  " код равен",                               //2
                                                  "Введите код задачи\n",                      //3
                                                  "Введите строку для проверки на полиндром\n",//4
                                                   "Строка является полиндромом",             //5
                                                   "Строка не является полиндромом",          //6
                                                   "Введите слова через пробел\n",             //7
                                                   "Введите натуральное число для" +
                                                   " подсчета различных цифр" +
                                                   " в его десятичной записи\n"                //8
        };
        public static void CPrintRusWord(int rus_word_position) => Console.Write(TextInformation[rus_word_position]);
        public static  void CPrint([In]string word)=>Console.Write(word);
        public static void CPrint([In] int word)=>Console.Write(word);
        public static void CprintArray([In]string[] s)
        {
            foreach(string s2 in s)
            {
                Console.Write(s2);
            }
            Console.WriteLine();
        }
        public static int CGetInt()=>Convert.ToInt32(Console.ReadLine());
        public static string GGetString()=>Console.ReadLine();
        public static void Exit() => Console.ReadLine();
    }
}
