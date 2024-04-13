// See https://aka.ms/new-console-template for more information
//https://products.codeporting.app/ru/convert/ai/csharp-to-python/
//https://www.codeconvert.ai/csharp-to-python-converter
namespace Lab1
{
    public class Program
    {
        static void Main(string[] args)
        {
            string f = "123 asdfgiiIIII  34 февраля 2021 года , 11 мая,   ________________" +
                "\n\n 2 Мая 1998-го года ,,,,,,,,,,," +
                "ууууууууууууууууrrrrYYYYYY11 июня 2011////" +
                "09 июня 2001 года, 11 Апрелят 2000 ------" +
                "111августа 2022 , ЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮ" +
                "-1 сентября 2011 года";
            var r=Lab1_task5_shared.Scan(f);
            foreach(string s in r)
            {
                Console.WriteLine(s);
            }
        }
    }
}
