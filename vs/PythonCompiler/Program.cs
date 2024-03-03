using System.Text;

namespace PythonCompiler
{
    internal static class Program
    {
        public static readonly Encoding encoding = Encoding.UTF8;
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Console.InputEncoding = encoding;
            Console.OutputEncoding = encoding;  
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.Run(new Form1());
        }
    }
}