using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;

internal static class TestLauncher
{
    private const string DefaultRenpyExe = @"F:\Tools\renpy-8.5.3-sdk\renpy.exe";

    [STAThread]
    private static void Main()
    {
        string projectDirectory = AppDomain.CurrentDomain.BaseDirectory.TrimEnd(
            Path.DirectorySeparatorChar,
            Path.AltDirectorySeparatorChar
        );

        string gameDirectory = Path.Combine(projectDirectory, "game");
        if (!Directory.Exists(gameDirectory))
        {
            ShowError("测试启动器必须放在游戏项目根目录，与 game 文件夹同级。");
            return;
        }

        string renpyExe = ResolveRenpyExecutable(projectDirectory);
        if (!File.Exists(renpyExe))
        {
            ShowError(
                "没有找到 Ren'Py SDK。\n\n" +
                "当前路径：" + renpyExe + "\n\n" +
                "请修改项目根目录中的 renpy-sdk-path.txt。"
            );
            return;
        }

        try
        {
            Process.Start(new ProcessStartInfo
            {
                FileName = renpyExe,
                Arguments = Quote(projectDirectory) + " run",
                WorkingDirectory = projectDirectory,
                UseShellExecute = true,
            });
        }
        catch (Exception exception)
        {
            ShowError("启动游戏失败：\n\n" + exception.Message);
        }
    }

    private static string ResolveRenpyExecutable(string projectDirectory)
    {
        string pathFile = Path.Combine(projectDirectory, "renpy-sdk-path.txt");

        if (File.Exists(pathFile))
        {
            string configuredPath = File.ReadAllText(pathFile).Trim().Trim('"');
            if (!string.IsNullOrEmpty(configuredPath))
            {
                return Environment.ExpandEnvironmentVariables(configuredPath);
            }
        }

        return DefaultRenpyExe;
    }

    private static string Quote(string value)
    {
        return "\"" + value.Replace("\"", "\\\"") + "\"";
    }

    private static void ShowError(string message)
    {
        MessageBox.Show(
            message,
            "剑来-书简湖问心局：测试启动器",
            MessageBoxButtons.OK,
            MessageBoxIcon.Error
        );
    }
}
