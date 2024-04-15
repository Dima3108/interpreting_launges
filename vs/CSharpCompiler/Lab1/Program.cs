// See https://aka.ms/new-console-template for more information
//https://products.codeporting.app/ru/convert/ai/csharp-to-python/
//https://www.codeconvert.ai/csharp-to-python-converter
namespace Lab1
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] urls =
            {
                "https://www.google.com/search?q=base64+code+table&oq=base64+code+ta&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBDIKCAUQABiABBiiBDIKCAYQABiABBiiBNIBCjIyNjU1ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8",
                "http://example.com/",
                "example.com",
                "погода.ру",
                "http://qwert.@@@@/g.ru",
                "https://www.dns-shop.ru/",
                "https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?stock=now-today-tomorrow-later&f[rv2z]=13iyb1&f[uq]=lxihi",
                "https://dotnet.microsoft.comen-us/apps/aspnet",
                "https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-8.0&WT.mc_id=dotnet-35129-website"
            };
            for(int i=0;i< urls.Length; i++)
            {
                Console.WriteLine(Lab5.checking_string_validity(urls[i]));
                try
                {
                   Console.WriteLine(Lab5.get_domain(urls[i]));
                }
                catch (Exception e)
                {
                    Console.WriteLine($"error:{e.Message}");
                }
            }
        }
    }
}
