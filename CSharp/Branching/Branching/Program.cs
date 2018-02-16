using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Branching
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your favorite number?");
            int favNum = Convert.ToInt32(Console.ReadLine());

            string result = favNum == 12 ? "You have an awesome favorite number." : "Your favorite number sucks.";

            Console.WriteLine(result);
            Console.ReadLine();

            //int roomTemperature = 70;

            //Console.WriteLine("Hi, what is your name?");
            //string name = Console.ReadLine();

            //Console.WriteLine("Hi, " + name + ", what is the temperature where you are?");
            //int currentTemperature = Convert.ToInt32(Console.ReadLine());

            //if (currentTemperature == roomTemperature)
            //{
            //    Console.WriteLine("It is exactly room temperature.");
            //}
            //else if (currentTemperature > roomTemperature)
            //{
            //    Console.WriteLine("It is warmer than room temp.");
            //}
            //else if (roomTemperature > currentTemperature)
            //{
            //    Console.WriteLine("It's colder than room temp.");
            //}
            //else
            //{
            //    Console.WriteLine("Something went wrong.");
            //}

            //Console.ReadLine();

            //int currentTemperature = 80;
            //int roomTemperature = 70;

            ////ternary branching
            //string comparisonResult = currentTemperature == roomTemperature ? "It is room temp." : "It is not room temp.";

            //Console.WriteLine(comparisonResult);
            //Console.ReadLine();

            //if (currentTemperature == roomTemperature)
            //{
            //    Console.WriteLine("It is exactly room temperature.");
            //}
            //else if (currentTemperature > roomTemperature)
            //{
            //    Console.WriteLine("It is warmer than room temperature.");
            //}
            //else if (roomTemperature > currentTemperature)
            //{
            //    Console.WriteLine("Room temp is warmer than current temp.");
            //}
            //else
            //{
            //    Console.WriteLine("It is not exactly room temperature.");
            //}
            Console.ReadLine();
        }
    }
}
