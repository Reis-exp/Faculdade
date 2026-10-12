<?php
include('layouts/header.php');

$nome = $_POST['nome'] ?? '';
$data_nascimento = $_POST['data_nascimento'] ?? '';

if ($nome == '' || $data_nascimento == '') {
    exit('Preencha todos os campos.');
}

$data = explode('-', $data_nascimento);

$ano = $data[0];
$mes = (int) $data[1];
$dia = (int) $data[2];

$data_comparacao = ($mes * 100) + $dia;

$signos = simplexml_load_file('signos.xml');

$signo_encontrado = null;

foreach ($signos->signo as $signo) {

    $inicio = explode('/', $signo->data_inicio);
    $dia_inicio = (int) $inicio[0];
    $mes_inicio = (int) $inicio[1];

    $fim = explode('/', $signo->data_fim);
    $dia_fim = (int) $fim[0];
    $mes_fim = (int) $fim[1];

    $data_inicio = ($mes_inicio * 100) + $dia_inicio;
    $data_fim = ($mes_fim * 100) + $dia_fim;

    if ($data_inicio > $data_fim) {

        if ($data_comparacao >= $data_inicio || $data_comparacao <= $data_fim) {
            $signo_encontrado = $signo;
            break;
        }

    } else {

        if ($data_comparacao >= $data_inicio && $data_comparacao <= $data_fim) {
            $signo_encontrado = $signo;
            break;
        }
    }
}
?>

<body>
    <div class="container mt-5">
        <div class="card shadow p-4">

            <h1>Resultado</h1>

            <?php if ($signo_encontrado != null) { ?>

                <h2>Olá, <?php echo $nome; ?>!</h2>

                <p>
                    Seu signo é
                    <strong><?php echo $signo_encontrado->nome; ?></strong>.
                </p>

                <h3>Características</h3>

                <p><?php echo $signo_encontrado->descricao; ?></p>

            <?php } else { ?>

                <p>Não foi possível identificar seu signo.</p>

            <?php } ?>

            <a href="index.php" class="btn btn-primary mt-3">Voltar</a>

        </div>
    </div>
</body>
</html>