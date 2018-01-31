<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="CS_006.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            font-family: Arial, Helvetica, sans-serif;
            color: #CC00FF;
        }
        .auto-style2 {
            width: 100%;
        }
        .auto-style3 {
            height: 23px;
        }
        .auto-style4 {
            background-color: #FF99FF;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h1>Head Line 1</h1>
        </div>
        <h2>Head Line 2</h2>
        <h3>Head Line 3</h3>
        <h4>Head Line 4</h4>
        <h5>Head Line 5</h5>
        <h6>Head Line 6</h6>
        <p class="auto-style1">
            This is some text I want to apply some style to.</p>
        <p>
            <a href="http://google.com">add hyperlink</a></p>
        <asp:HyperLink ID="HyperLink1" runat="server" NavigateUrl="http://www.yahoo.com">This is another hyperlink</asp:HyperLink>
        <p>
            <asp:Image ID="Image1" runat="server" ImageUrl="~/1200px-Bucephala-albeola-010.jpg" />
        </p>
    </form>
    <table class="auto-style2">
        <tr>
            <td class="auto-style3">Player</td>
            <td class="auto-style3">Year</td>
        </tr>
        <tr>
            <td>Sammy Sosa</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Mark MacGuire</td>
            <td>2005</td>
        </tr>
    </table>
    <p>
        &nbsp;</p>
    <ol>
        <li>First Item ol</li>
        <li>Second Item</li>
        <li>Third Item</li>
    </ol>
    <ul>
        <li class="auto-style4">This is ul</li>
        <li class="auto-style4">no order</li>
        <li class="auto-style4">all equal</li>
    </ul>
    <p>
        &nbsp;</p>
    <p>
        &nbsp;</p>
</body>
</html>
