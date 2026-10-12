<?php include('layouts/header.php'); ?>

<body>

    <div class="container mt-5">

        <div class="card shadow p-4">

            <h1 class="mb-4">
                Bem-vindo ao sistema de identificação do seu signo!
            </h1>

            <h3>
                Descubra seu signo preenchendo o formulário abaixo:
            </h3>

            <form action="show_zodiac_sign.php" method="post">

                <div class="mb-3">
                    <label for="nome" class="form-label">
                        Digite seu nome:
                    </label>

                    <input type="text" name="nome" id="nome" class="form-control" required >
                </div>

                <div class="mb-3">
                    <label for="data_nascimento" class="form-label">
                        Digite sua data de nascimento:
                    </label>

                    <input type="date" name="data_nascimento" id="data_nascimento" class="form-control" required >
                </div>

                <button type="submit" class="btn btn-primary">
                    Descobrir signo
                </button>

            </form>

        </div>

    </div>

</body>
</html>