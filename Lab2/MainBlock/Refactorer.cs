using Lab2.Processing;

namespace Lab2.MainBlock
{
    internal class Refactorer
    {
        private string charsToDel = ".,!?()\"\'-=+“1234567890”—[]:;–/\\«»%&#{}_";
        private string defaultSourse = "../../../Docs";

        public Refactorer()
        {
            TxtFilesOperator fileWorker = new TxtFilesOperator();

            var text = fileWorker.InputFromSourse(defaultSourse + "/kapital.txt").Result;

            TextEditor textEditor = new TextEditor(text, charsToDel);

            text = textEditor.RefactorThis();

            var srs = fileWorker.OutputInFile(defaultSourse, text);

            Console.WriteLine("Result text is in " + srs);
        }
    }
}
