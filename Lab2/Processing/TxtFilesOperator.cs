namespace Lab2.Processing
{
    internal class TxtFilesOperator
    {
        private string filePath;
        private string fileOut;

        public string FilePath { get => filePath; set => filePath = value; }
        public string FileOut { get => fileOut; set => fileOut = value; }

        public async Task<string> InputFromSourse(string sourse)
        {
            try
            {
                FilePath = sourse;
                if (!File.Exists(filePath))
                {
                    Exception ex = new Exception("Файл не найден.");
                }

                string content = File.ReadAllText(filePath).ToLower();
                return content;
            }
            catch
            {
                Exception ex = new Exception("Ошибка при чтении файла.");
                return ex.Message;
            }
        }

        public async Task<string> OutputInFile(string sourse, string text)
        {
            try
            {
                FileOut = Path.Combine(sourse, "result.txt");
                if (!File.Exists(FileOut))
                {
                    using (var stream = File.Create(fileOut)) { }
                    await File.WriteAllTextAsync(fileOut, text);
                }
                else
                {
                    Exception ex = new Exception("Файл " + FileOut + " уже создан.");
                }
                return FileOut;
            }
            catch
            {
                Exception ex = new Exception("Ошибка при чтении файла.");
                return ex.Message;
            }
        }
    }
}