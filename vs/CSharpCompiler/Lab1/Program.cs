// See https://aka.ms/new-console-template for more information
//https://products.codeporting.app/ru/convert/ai/csharp-to-python/
//https://www.codeconvert.ai/csharp-to-python-converter
namespace Lab1
{
    public class Program
    {
        static void Main(string[] args)
        {
            string inp_w = File.ReadAllText("ОжеговСИ.txt");
            char letter = (Console.ReadLine())[0];
            var res = Lab4_task2.TextScanner(inp_w, letter);
            foreach (var line in res)
            {
                Console.WriteLine(line);
            }
            Console.WriteLine(res.Length);
        }
    }
}
