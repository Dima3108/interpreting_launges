using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab1
{
    public class Lab1_task5_shared
    {
        public static List<string>Scan(string input)
        {
            string[] months =new string [12]{"января","февраля","марта","апреля","мая","июня",
            "июля","августа","сентября","октября","ноября","декабря"};
            int mlen = months[0].Length;
            for(int j=1;j<months.Length;j++)
                if (months[j].Length > mlen)
                    mlen = months[j].Length;
            string cesh = "";
            List<string> result = new List<string>();
            int pos = 0;
            
            string month_ = "";
            bool suc = false;
            int flag1 = 0;
            foreach (char _char_ in input.ToLower().ToCharArray())
            {
                if (pos == 0)
                {
                    if(_char_>='0'&& _char_ <= '9')
                    {
                        cesh = _char_.ToString();
                        pos = 1;
                    }
                    else
                    {
                        pos = 0;
                        cesh = "";
                        
                    }
                }
                else
                {
                    if (pos <3)
                    {
                        if(_char_==' ')
                        {
                            pos = 3;
                            suc = false;
                            cesh+= _char_.ToString();
                        }
                        else
                        {
                            if (_char_ >= '0' && _char_ <= '9')
                            {
                                cesh+= _char_.ToString();
                                pos = 2;
                            }
                            else
                            {
                                pos = 0;
                                cesh = "";
                               
                            }
                        }
                    }
                    else
                    {
                        if (flag1 == 0)
                        {
                            if (_char_ != ' ')
                            {
                                if (month_.Length <= mlen)
                                {
                                    cesh += _char_.ToString();
                                    month_ += _char_.ToString();
                                    suc = false;
                                    foreach (string _m in months)
                                        if (_m.Contains(month_))
                                        {
                                            if (_m.Length >= month_.Length)
                                            {
                                                suc = true;
                                                break;
                                            }
                                        }
                                    if (!suc)
                                    {
                                        cesh = "";
                                        
                                        month_ = "";
                                        pos = 0;
                                    }
                                }
                            }
                            else
                            {
                                cesh += _char_.ToString();
                                flag1 = 1;
                            }
                        }
                        else
                        {
                            if (_char_ >= '0' && _char_ <= '9')
                            {
                                flag1 = 2;
                                cesh+= _char_.ToString();

                            }
                            else
                            {
                                if (flag1 == 2)
                                {
                                    result.Add(cesh);
                                    pos = 0;
                                    cesh = "";
                                    month_ = "";
                                    flag1 = 0;
                                }
                                else
                                {
                                    pos = 0;
                                    cesh = "";
                                    month_ = "";
                                    flag1 = 0;
                                }
                            }
                        }
                    }
                }
            }
            return result;
        }
    }
}
