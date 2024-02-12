using System;
using System.Runtime;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
namespace ForPython
{
    
    public class HelpFunctions
    {
        public static string[] TextInformation = { "Выберите задачу, которую хотите решить\n",
                                                  "у задачи "," код равен",
                                                  "Введите код задачи"};
        public static void CPrintRusWord(int rus_word_position) => Console.Write(TextInformation[rus_word_position]);
        public static  void CPrint([In]string word)=>Console.Write(word);
        public static void CprintArray([In]string[] s)
        {
            foreach(string s2 in s)
            {
                Console.Write(s2);
            }
            Console.WriteLine();
        }
    }
}
