// See https://aka.ms/new-console-template for more information
//https://products.codeporting.app/ru/convert/ai/csharp-to-python/
//https://www.codeconvert.ai/csharp-to-python-converter
namespace Lab1
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("27-99a.txt");
            int[]val=new int[lines.Length-1];
            for(int i=0;i<val.Length;i++)
            {
                val[i] = int.Parse(lines[i+1]);
            }
            Console.WriteLine(Lab4_task1.GetIndex(val));
            lines = File.ReadAllLines("27-99b.txt");
            val = new int[lines.Length - 1];
            for (int i = 0; i < val.Length; i++)
            {
                val[i] = int.Parse(lines[i + 1]);
            }
            Console.WriteLine(Lab4_task1.GetIndex(val));
        }
    }
}
