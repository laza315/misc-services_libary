using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Predavanje_2
{
    internal class Kontakt
    {
        public int IdBroj {  get; set; }

        public string Ime { get; set; }

        public string Prezime { get; set; }

        public string Mesto { get; set; }

        public string Adresa { get; set; }

        public string Telefon { get; set; }

        public string Ispis()
        {
            return string.Format("{0};{1};{2};{3};{4};{5};",
                IdBroj, Ime, Prezime, Mesto, Adresa,Telefon);
        }
    }

}

