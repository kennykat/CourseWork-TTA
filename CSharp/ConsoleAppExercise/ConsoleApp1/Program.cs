using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("What is your favorite number?");
            string favoriteNumber = Console.ReadLine();
            int favNum = Convert.ToInt32(favoriteNumber);
            int total = favNum * 50;
            Console.WriteLine(favNum + " multiplied by 50 is " + total + ".");
            Console.WriteLine();
            //Console.ReadLine();

            Console.WriteLine("How old are you?");
            string ageInput = Console.ReadLine();
            int age = Convert.ToInt32(ageInput);
            int totalAge = age + 25;
            int youngAge = age - 12.5;
            Console.WriteLine("In 25 years you will be " + totalAge + " years old.");
            Console.ReadLine();



        }
    }
}
