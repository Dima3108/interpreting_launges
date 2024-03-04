namespace PythonCompiler
{
    using System;
    using System.Text;
    using IronPython.Hosting;
    using IronPython.Compiler;
    using IronPython.Modules;
    using IronPython.Runtime;
    using Microsoft.Scripting.Hosting;
    using Mono.Unix.Native;
    using Microsoft.Scripting.Hosting.Providers;
    using Microsoft.Scripting.Runtime;
    using Microsoft.Scripting;
   // using Python.Runtime;//https://www.codeproject.com/Questions/5362420/Running-Python-script-in-Csharp-without-installing
    public class Result : ErrorSink
    {
        public override void Add(SourceUnit source, string message, SourceSpan span, int errorCode, Severity severity)
        {
            Add(message, source.Path, null, null, span, errorCode, severity);
        }

        public override void Add(string message, string path, string code, string line, SourceSpan span, int errorCode, Severity severity)
        {
            if (severity == Severity.Ignore)
                return;

            // Collect diagnostics here.
        }
    }
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.DefaultExt = ".py";
            openFileDialog1.CheckPathExists = true;
            openFileDialog1.CheckFileExists = true;
            openFileDialog1.Multiselect = false;
            var result = openFileDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(File.Exists(textBox1.Text))
            {
                try
                {
                    var engine = Python.CreateEngine();

                    var fileName = textBox1.Text;
                    var source = engine.CreateScriptSourceFromString(File.ReadAllText(fileName), fileName, SourceCodeKind.File);
                    var comp_=source.Compile();
                    comp_.Execute();    
                   /* var sourceUnit = HostingHelpers.GetSourceUnit(source);

                    var result = new Result();
                    var context = new CompilerContext(sourceUnit, new PythonCompilerOptions(), result);
                    var parser = Parser.CreateParser(context, new PythonOptions());
                    parser.ParseFile(false);*/

                }
                catch (Exception error)
                {
                    Console.WriteLine(error.Message);
                    Console.WriteLine(error.StackTrace);
                    Console.WriteLine(error.Source);
                }
                Console.WriteLine($"скрипт {openFileDialog1.SafeFileName} завершил свою работу!");

            }
        }
    }
}
