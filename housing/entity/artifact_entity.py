from collections import namedtuple

# This is for the outputs of the components

DataIngestionArtifact = namedtuple("DataIngestionArtifact",['train_file_path',
                                                            'test_file_path',
                                                            'is_ingested',
                                                            'message'])

