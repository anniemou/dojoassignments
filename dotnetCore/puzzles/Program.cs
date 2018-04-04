using System;
using System.Linq;
using System.Threading;

namespace puzzles
{
    class Program
    {
        static void Main(string[] args)
        {
            RandomArray();
            TossCoin();
            Names();
        }

        
        public static int[] RandomArray()
        {
            // Ftiaxnw ena kainourgio adeio array apo integers me 10 theseis
            var rndArr = new int[10];
            var min = 25;
            var max = 5;
            var sum = 0;

            // Efoson thelw 10 arithmous, kanw mia loop apo to 1 mexri to 10
            for (int i = 0; i < 10; i++)
            {
                // Gia na parw enan tyxaio arithmo apo to 5 ews to 25, xrhsimopoiw thn Random
                Random rnd = new Random();
                var randomNumber = rnd.Next(5, 26);

                //Ean to min einai pio megalo apo ton arithmo pou exw twra, tote o kainourgios arithmos einai pio mikros
                if (min > randomNumber)
                {
                    min = randomNumber;
                }

                if (max < randomNumber)
                {
                    max = randomNumber;
                }

                // Dinw sthn thesh i (px 0, 1, 2, 3 klp) ton arithmo apo epanw
                rndArr[i] = randomNumber;

                sum += randomNumber;
            }

            Console.WriteLine($"Min: {min}");
            Console.WriteLine($"Max: {max}");
            Console.WriteLine($"Sum: {sum}");

            return rndArr;
        }

        public static string TossCoin()
        {
            // Krataw sthn timh 0 to heads kai sthn 1 to tails
            var coinSide = new string[] {"Heads", "Tails"};

            Console.WriteLine("Tossing a Coin!");
            
            // Pairnw tyxaia 0 h' 1 (san an epairna dyo pleyres dld). Edw bazw mexri to 2, giati to 2 DEN symperilambanetai.
            // Opote ousiastika einai apo to 0 mexri to 1.
            Random rnd = new Random();
            var randomNumber = rnd.Next(0, 2);
            
            Console.WriteLine(randomNumber);
            
            // Me oti pleyra phra, kanthn alfarithmitiko apo to array pou exw ta keimena
            Console.WriteLine($"It's a {coinSide[randomNumber]}");

            return coinSide[randomNumber];
        }

        public static string[] Names()
        {
            var names = new string[] {"Todd", "Tiffany", "Charlie", "Geneva", "Sydney"};

            for (int i = 0; i < names.Length - 1; i++)
            {
                var oldValue = names[i];
                
                Random rnd = new Random();
                var randomNumber = rnd.Next(0, names.Length);

                var newValue = names[randomNumber];

                names[i] = newValue;
                names[randomNumber] = oldValue;
            }

            return names.Where(name => name.Length > 5).ToArray();
        }

    }
}
