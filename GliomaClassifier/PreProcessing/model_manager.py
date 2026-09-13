import logging
import os
import slicer

MODEL_METADATA = {
    "ResNet10": {
        "url": (
            "https://github.com/xristosand/SlicerGliomaAI/releases/"
            "download/v1.0.0/resnet10_full_torchscript_ep25.pt"
        ),
        "checksum": (
            "SHA256:"
            "042d2d49919feff625c139bf1280237675c0b3ffd00f168e573ce5c763049c08"
        ),
    },
    "ResNet50": {
        "url": (
            "https://github.com/xristosand/SlicerGliomaAI/releases/"
            "download/v1.0.0/resnet50_full_torchscript.pt"
        ),
        "checksum": (
            "SHA256:"
            "cc31d224550e0d0b1e484998c486aa7174d4520e9ef055ecb437e00df0b0e58b"
        ),
    },
    "DenseNet121": {
        "url": (
            "https://github.com/xristosand/SlicerGliomaAI/releases/"
            "download/v1.0.0/densenet121_full_torchscript.pt"
        ),
        "checksum": (
            "SHA256:"
            "e0b0f968433a6d01800c06d0e7a312b7b2de7838b6d47492909314e95b83ff46"
        ),
    },
}


def ensure_model(model_name, model_path):
    """Download and verify an optional model before returning its local path."""

    if model_name not in MODEL_METADATA:
        raise ValueError(f"Unknown model: {model_name}")

    metadata = MODEL_METADATA[model_name]
    url = metadata["url"]
    checksum = metadata["checksum"]

    model_directory = os.path.dirname(model_path)
    os.makedirs(model_directory, exist_ok=True)

    model_already_exists = os.path.isfile(model_path)
    operation = "Verifying" if model_already_exists else "Downloading"

    progress = slicer.util.createProgressDialog(
        windowTitle="GliomaAI",
        labelText=(
            f"{operation} {model_name}...\n"
            "Downloaded models are verified using SHA-256."
        ),
        maximum=0,
    )

    try:
        success = slicer.util.downloadFile(
            url,
            model_path,
            checksum=checksum,
            reDownloadIfChecksumInvalid=True,
        )

        if not success:
            # Do not retain an incomplete or checksum-invalid download.
            if os.path.isfile(model_path):
                try:
                    os.remove(model_path)
                except OSError:
                    logging.warning(
                        "Could not remove invalid model file: %s",
                        model_path,
                    )

            raise RuntimeError(
                f"Unable to download or verify {model_name}. "
                "Please check the internet connection and try again."
            )

        if not os.path.isfile(model_path):
            raise RuntimeError(
                f"{model_name} verification completed, "
                "but the model file was not found."
            )

        if model_already_exists:
            logging.info("%s checksum verification succeeded.", model_name)
            print(
                f"[GliomaAI] {model_name}: "
                "Loaded from verified local storage.\n"
            )
        else:
            logging.info(
                "%s downloaded and verified successfully.",
                model_name,
            )
            print(
                f"[GliomaAI] {model_name}: "
                "Download and SHA-256 verification completed successfully.\n"
            )

        return model_path

    except Exception:
        logging.exception(
            "Model retrieval or verification failed for %s.",
            model_name,
        )
        raise

    finally:
        progress.close()