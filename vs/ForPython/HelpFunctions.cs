using System;
using System.Runtime;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
namespace ForPython
{
    
    public class HelpFunctions
    {
        
        public static  void CPrint([In]string word)=>Console.WriteLine(word);
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
