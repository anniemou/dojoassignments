using System;

namespace Wizard_Ninja_Samural
{
    class Samurai : Human
    {
        // To Samurai klhrwnomei apo to Human. To "base" anaferete sthn class Human, h opoia exei constructor me to toulaxiston 1 parametro
        // opote kaloume thn "base" me thn parametro pou diabazoume sto Samurai, kai ononmazete "name"
        public Samurai(string name) : base(name)
        {
            this.Health = 200;
        }

        public void DeathBlow(object target)
        {
            Human enemy = target as Human;
            if (enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                // Ean to enemy health einai mikrotero apo 50, thelw na to kanw 0
                if (enemy.Health < 50)
                {
                    enemy.Health = 0;
                }
            }
        }

        public void Meditate()
        {
            this.Health = 200;
        }
    }
}