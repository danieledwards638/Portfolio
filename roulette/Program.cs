using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace roulette
{

    class program
    {

        static void Main(string[]args)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Random ran = new Random();
            var r = new Random();
            string[] color = { "Red", "Black" };
            string guess;
            int attempts = 0;
            int bet;
            int money = 500;
            while(money!=0)
            {
                Console.WriteLine("Roulette Roller by Daniel\n");
                Console.WriteLine("Money:$" + money+"          Attempts:"+attempts);
                Console.WriteLine("Type in any of the following letters below:");
                Console.WriteLine("a.Even b.Odd  c.1-18  d.19-36");
                Console.WriteLine("e.Red f.Black g.1-12  h.13-24");
                Console.WriteLine("i.3rd 12");
                guess = (Console.ReadLine());
                //guess verifier
                guess.ToLower();
                bool check = guess == "a" || guess == "b" || guess == "c" || guess == "d" || guess == "e" || guess == "f" || guess == "g" || guess == "h" || guess == "i";
                if (check == false)
                {
                    Console.WriteLine("You did not enter the correct input value (even/odd)");
                    Console.ReadKey();
                    Console.Clear();
                    continue;
                }
                else
                {
                    bet:
                        Console.WriteLine("Enter an amount to bet.");
                        bet=Convert.ToInt32(Console.ReadLine());
                        //bet verifier
                        if (bet > money)
                        {
                            Console.WriteLine("You do not have enough money!");
                            Console.WriteLine("Please try again");
                            Console.ReadKey();
                            goto bet;
                        }
                        else
                        {
                            money -= bet;
                            int roll = ran.Next(0,37);
                            string ranColor = color[r.Next(color.Length)];
                            bool even = roll % 2 == 0;
                            if (((((guess=="a") && (even==true))) || ((guess=="b") && (even==false))) || ((guess=="e")&&(ranColor=="Red") || (guess=="f")&&(ranColor=="Black")))
                            {
                                Console.WriteLine("The roulette rolled: " + ranColor + " " + roll);
                                Console.WriteLine("You won! +$" + bet * 2 + "!");
                                Console.WriteLine("<Press enter to continue>");
                                money += bet * 2;
                                attempts += 1;
                                Console.ReadKey();
                            }

                            else if ((guess=="c") && ((roll>0)&&(roll<19)))
                            {
                                Console.WriteLine("The roulette rolled: " + ranColor + " " + roll);
                                Console.WriteLine("You won! +$" + bet * 2 + "!");
                                Console.WriteLine("<Press enter to continue>");
                                money += bet * 2;
                                attempts += 1;
                                Console.ReadKey();
                            }
                            else if ((guess=="d") && ((roll>18)&&(roll<37)))
                            {
                                Console.WriteLine("The roulette rolled: " + ranColor + " " + roll);
                                Console.WriteLine("You won! +$" + bet * 2 + "!");
                                Console.WriteLine("<Press enter to continue>");
                                money += bet * 2;
                                attempts += 1;
                                Console.ReadKey();
                            }
                            else if ((guess=="g")&&(roll>0 && roll<13)||(guess=="h")&&(roll>12 && roll < 25)||(guess=="i")&&(roll>24&&roll<37))
                            {
                                Console.WriteLine("The roulette rolled: " + ranColor + " " + roll);
                                Console.WriteLine("You won! +$" + bet * 2 + "!");
                                Console.WriteLine("<Press enter to continue>");
                                money += bet * 3;
                                attempts += 1;
                                Console.ReadKey();
                            }
                            else
                            {
                                Console.WriteLine("The roulette rolled: " + ranColor + " " + roll);
                                Console.WriteLine("You lost! -$" + bet + "!");
                                Console.WriteLine("<Press enter to continue>");
                                attempts += 1;
                                Console.ReadKey();
                                if (money==0)
                                {
                                    Console.WriteLine("You are out of money.");
                                    Console.WriteLine("<Press enter to continue>");
                                    Console.ReadKey();
                                }
                            }
                        }
                }
            Console.Clear();
            }

        }
    }
}

