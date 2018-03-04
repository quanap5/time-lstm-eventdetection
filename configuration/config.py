run_config = {'Xserver': True,
              'log_file': 'logs/run.logs',
              'experiment_id': "Result of running LSTM 6",
              #'data_folder': 'resources/data/earthquake/Earthquake1/',
              #'data_folder': 'resources/data/earthquake/Earthquake2/',
              #'data_folder': 'resources/data/earthquake/Earthquake3/',
              #'data_folder': 'resources/data/earthquake/Earthquake4/',
              #'data_folder': 'resources/data/earthquake/Earthquake5/',
              'data_folder': 'resources/data/earthquake/Earthquake6/',
              'save_figure': True
              }


multi_step_lstm_config = {'batch_size': 512,
                          'n_epochs': 50,
                          'dropout': 0.2,
                          'look_back': 1,
                          'look_ahead': 1,
                          'layers': {'input': 1, 'hidden1': 64, 'hidden2': 256, 'hidden3': 100, 'output': 1},
                          'loss': 'mse',
                          # 'optimizer': 'adam',
                          'train_test_ratio': 0.7,
                          'shuffle': False,
                          'validation': True,
                          'learning_rate': .01,
                          'patience': 20,
                          }
