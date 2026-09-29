from typing import Any

from loguru import logger
import ollama
import tiktoken

from app.constants import ENCODING_NAME, FEW_SHOT_PROMPT, MAX_INPUT_TOKENS, MODEL_NAME


class OllamaClient:
    def __init__(self) -> None:
        self.model_name = MODEL_NAME
        self.few_shot_prompt = FEW_SHOT_PROMPT
        self.encoder = tiktoken.get_encoding(ENCODING_NAME)

    def chat(self, text: str) -> Any:
        prompt = self._build_prompt(text)
        tokens = self._tokenize(prompt)

        if not self._check_tokens(tokens):
            prompt = self._truncate_prompt(tokens)
            tokens = self._tokenize(prompt)

        try:
            response: ollama.ChatResponse = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
            )
        except Exception:
            logger.exception('Error while communicating with Ollama')
            raise

        prompt_tokens = response.prompt_eval_count
        completion_tokens = response.eval_count
        logger.info(
            f'Successful response: prompt_tokens={prompt_tokens} completion_tokens={completion_tokens}'
        )

        return response, tokens

    def _build_prompt(self, text: str) -> str:
        prompt = self.few_shot_prompt + '\n' + 'Текст для обработки:' + text
        return prompt

    def _tokenize(self, text: str) -> list[int]:
        tokens = self.encoder.encode(text)
        return tokens

    def _check_tokens(self, tokens: list[int]) -> bool:
        if len(tokens) > MAX_INPUT_TOKENS:
            logger.error(
                f'MAX_INPUT_TOKENS limit was exceeded: MAX{MAX_INPUT_TOKENS} CURR:{len(tokens)}'
            )
            return False
        return True

    def _truncate_prompt(self, tokens: list[int]) -> str:
        logger.warning(f'Text was truncated:MAX={MAX_INPUT_TOKENS} CURR={len(tokens)}')
        truncated_tokens = tokens[:MAX_INPUT_TOKENS]
        return self.encoder.decode(truncated_tokens)
