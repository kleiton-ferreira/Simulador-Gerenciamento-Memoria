import time
from memoria import Memoria
from algoritmos import first_fit, best_fit, worst_fit


def simular_algoritmo(algoritmo, nome_algoritmo, processos):
    memoria = Memoria()
    print(f"\n--- Simulação com {nome_algoritmo} ---")

    for processo_id, tamanho in processos:
        print(f"\nAlocando processo P{processo_id} de {tamanho} KB...")
        sucesso = memoria.alocar_processo(processo_id, tamanho, algoritmo)

        if sucesso:
            print("✅ Alocação bem-sucedida.")
        else:
            print("❌ Falha na alocação. Memória cheia ou fragmentada.")

        print("Estado atual da memória:", memoria)
        time.sleep(1)

    print("\nLiberando processos...")
    for processo_id, _ in processos:
        memoria.liberar_processo(processo_id)
        print(f"🔄 Processo P{processo_id} liberado.")
        print("Estado atual da memória:", memoria)
        time.sleep(1)

    print("🏁 Memória liberada. Estado final:", memoria)


if __name__ == "__main__":
    processos_exemplo = [
        (1, 20), (2, 30), (3, 10), (4, 40), (5, 50), (6, 5)
    ]

    simular_algoritmo(first_fit, "First Fit", processos_exemplo)
    simular_algoritmo(best_fit, "Best Fit", processos_exemplo)
    simular_algoritmo(worst_fit, "Worst Fit", processos_exemplo)
