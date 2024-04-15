using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab5
    {
        public static bool checking_string_validity(string url)
        {
            return checking_string_validity(url, out string t);
        }
        public static string get_domain(string url)
        {
            string dom = "";
            if(!checking_string_validity(url,out  dom))
            {
                throw new Exception("Некорректное имя домена!");
            }
            //http
            char[] ch = url.ToLower().ToCharArray();
            int strat_pos = 4;
            if (ch[strat_pos] == 's')
                strat_pos++;
            strat_pos += 3;
            dom = "";
            while (ch[strat_pos]!='/')
            {
                dom += ch[strat_pos++].ToString();
            }
            return dom;
        }
        private static bool checking_string_validity(string url,out string domain_)
        {
            string start_val = "http";
            domain_ = "";
            if(url==null||url.Length<=start_val.Length)
                return false;
            string tmp = "";
            string http_no_secure = "http:";
            string http_secure = "https:";
            string domain = "";
            int last_point_position = 0;
            int pos = 0;
            int flag1 = 0,flag2=0,flag3=0;
            string domain_zone = "";
            string the_rest_of_the_way = "";
            foreach (char c in url.ToLower().ToCharArray())
            {
                if (pos < start_val.Length)
                {
                      tmp += c.ToString();
                      pos++;
                }
                else if(c!='/' && flag1==0)
                {
                    {
                        if (c != 's' && c != ':')
                            return false;
                        else
                        {
                            tmp += c.ToString();
                            pos++;
                            if (c == ':')
                            {
                                if (tmp != http_no_secure && tmp != http_secure)
                                    return false;
                            }
                        }
                    }
                }
                else
                {
                    tmp += c.ToString();
                    pos++;
                    if (c == '/' && flag1==0)
                    {
                        flag1 = 1;
                        if (tmp != (http_no_secure + '/'.ToString()) && tmp != (http_secure + "/".ToString()))
                        {
                            return false;
                        }
                    }
                    else if (flag1 == 1 && flag2 == 0)
                    {
                        last_point_position = -1;
                        int pos2 = pos+1;
                        char[]c_url=url.ToCharArray();
                        while ((pos2 < c_url.Length) && (c_url[pos2]!='/'))
                        {
                            if (c_url[pos2] == '.')
                            {
                                last_point_position = pos2;
                            }
                            pos2++;
                        }
                        if (last_point_position < 0)
                            return false;
                        flag2 = 2;
                    }
                    else 
                    {
                        if ((pos < last_point_position)&& c!='/')
                        {
                             domain += c.ToString();
                        }
                        else if(pos==last_point_position)
                        {
                             string table = "qwertyuiopasdfghjklzxcvbnm.1234567890-";
                             foreach (char v in domain.ToCharArray())
                             if (table.Contains(v) == false)
                                 return false;
                        }
                        else 
                        {
                            if (flag3 == 0)
                            {
                                if (c != '/')
                                {
                                    if (c != '.')
                                        domain_zone += c.ToString();
                                }
                                else
                                {
                                    string table_domain = "qwertyuiopasdfghjklzxcvbnm";
                                    foreach (char v in domain_zone.ToCharArray())
                                        if (table_domain.Contains(v) == false)
                                            return false;
                                    flag3 = 1;
                                }
                            }
                            else
                            {
                                the_rest_of_the_way += c.ToString();
                            }
                        }
                        
                    }
                    
                    
                }
            }
            if (the_rest_of_the_way.Length > 0)
            {
                string url_full_char_table = "qwertyuiopasdfghjklzxcvbnm/?&+;#1234567890-=._[]";
                foreach (char c in the_rest_of_the_way.ToCharArray())
                    if (url_full_char_table.Contains(c) == false)
                        return false;
            }
            domain_ = domain+"."  + domain_zone;
            return true;
        }
    }
}
