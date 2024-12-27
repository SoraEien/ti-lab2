using System.Text;
using System.Text.RegularExpressions;

namespace Lab2.Processing
{
    internal class TextEditor
    {
        private string text;
        private string charsToDelete;

        public TextEditor() { }

        public TextEditor(string text) : this()
        {
            this.text = text;
        }

        public TextEditor(string text, string charsToDelete) : this(text)
        {
            this.charsToDelete = charsToDelete;
        }

        public string RefactorThis()
        {
            try
            {
                text = text.ToLower();

                text = text.Replace("\r", " ");
                text = text.Replace("\n", " ");
                text = Regex.Replace(text, @"s{2,}", " ").Trim();

                var result = new StringBuilder();

                foreach (char ch in text)
                {
                    if (!charsToDelete.Contains(ch))
                    {
                        result.Append(ch);
                    }
                }

                return result.ToString();
            }
            catch
            {
                Exception ex = new Exception("Ошибка при удалении симвлов.");
                return ex.Message;
            }
        }
    }
}
