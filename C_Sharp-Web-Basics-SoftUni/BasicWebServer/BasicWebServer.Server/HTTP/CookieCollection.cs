﻿
namespace BasicWebServer.Server.HTTP
{
    using System.Collections;

    public class CookieCollection : IEnumerable<Cookie>
    {
        private readonly Dictionary<string, Cookie> cookies;


        public CookieCollection()
        {
            this.cookies = new Dictionary<string, Cookie>();
        }



        public string this[string name] => this.cookies[name].Value;

        //public int Count => this.cookies.Count;

        public bool Contains(string name) => this.cookies.ContainsKey(name);



        public void Add(string name, string value)
        {
            this.cookies[name] = new Cookie(name, value);
        }


        public IEnumerator<Cookie> GetEnumerator()
        {

            return this.cookies.Values.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return this.GetEnumerator();
        }
    }
}
