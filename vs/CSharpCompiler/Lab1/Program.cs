// See https://aka.ms/new-console-template for more information
//https://products.codeporting.app/ru/convert/ai/csharp-to-python/
//https://www.codeconvert.ai/csharp-to-python-converter
namespace Lab1
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] a = {"aaa22345!`sdEEE",
                           "1234567890",
                           "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"};
            string[] b = Lab1_task4.task_10(a);
            foreach (string s in b)
            {
                Console.WriteLine(s);
            }
        }
    }
}
