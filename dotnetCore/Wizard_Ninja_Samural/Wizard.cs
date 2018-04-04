using System;

namespace Wizard_Ninja_Samural
{
    class Wizard : Human
    {
        // To Wizard klhrwnomei apo to Human. To "base" anaferete sthn class Human, h opoia exei constructor me to toulaxiston 1 parametro
        // opote kaloume thn "base" me thn parametro pou diabazoume sto Wizard, kai ononmazete "name"
        public Wizard(string name) : base(name)
        {
            this.Health = 50;
            this.Intelligence = 25;
        }

        public void Heal()
        {
            this.Health = this.Intelligence * 10;
        }

        public void Fireball(object target)
        {
            Human enemy = target as Human;
            if (enemy == null)
            {
                Console.WriteLine("Failed Attack");
            }
            else
            {
                // Pairnw tyxaio arithmo apo to 20 ews to 51
                Random rnd = new Random();
                var attack = rnd.Next(20, 51);
                
                // Afairw to health apo ton enemy me bash thn timh pou phra apo epanw
                enemy.Health -= attack;
            }
        }
    }
}