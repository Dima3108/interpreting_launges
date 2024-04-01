using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab4_task2
    {
        public static string[] TextScanner(string words,char letter)
        {
            var result = new List<string>();
            char let_ = (letter.ToString().ToLower().ToCharArray())[0];            
            foreach(string word in words.Split(new char[] {' ',',','.','-','!',';','/','?',':','\t','\r','\n'}))
            {
                if (word != null && word.Length > 0)
                {
                    if ((word.ToLower())[0] == let_)
                    {
                        result.Add(word);
                    }
                }
            }
            return result.ToArray();
        }
    }
}
