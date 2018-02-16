using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VariablesAndDataTypes
{
    class Program
    {
        static void Main(string[] args)
        {

            //Console.WriteLine("What is your name?");
            //string yourName = Console.ReadLine();
            //Console.WriteLine("Your name is: " + yourName);
            //Console.ReadLine();
            ////assign value to variable and use
            ////same variable in program later on

            //Console.WriteLine("What is your favorite number?");
            //string favoriteNumber = Console.ReadLine();
            //int favNum = Convert.ToInt32(favoriteNumber);
            //int total = favNum + 5;
            //Console.WriteLine("Your favorite number plus 5 is: " + total);
            //Console.ReadLine();

            bool isStudying = false;
            byte hoursWorked = 42;
            sbyte currentTemperature = -23;
            char questionMark = '\u2103';

            decimal moneyInBank = 100.5m;
            //when using a decimal, you have to add the m so compiler knows what it is

            double heightInCentimeters = 211.20323209;

            float secondsLeft = 2.62f;
            //f is for float, so compiler knows what it is
            //f for float, m for decimal

            short temperatureOnMars = -341;

            string myName = "Kendra";

            int currentAge = 30;
            string yearsOld = currentAge.ToString();
            //toString converts data type to string

            bool isRaining = true;
            string rainingStatus = Convert.ToString(isRaining);

            Console.WriteLine(rainingStatus);
            Console.ReadLine();
        }
    }
}
