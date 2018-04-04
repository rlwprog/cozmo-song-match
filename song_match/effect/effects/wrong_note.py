from cozmo.anim import Triggers

from song_match.effect import Effect


class WrongNoteEffect(Effect):

    async def play(self, cube_id: int, is_player: bool = True) -> None:
        """Play the wrong note effect.

        * Play ``WrongNoteEffect.wav``
        * Animate Cozmo with :attr:`~cozmo.anim.Triggers.MemoryMatchPlayerLoseHand` or
          :attr:`~cozmo.anim.Triggers.MemoryMatchCozmoLoseHand` depending upon ``is_player``.
        * Flash the incorrect cube red.

        :param cube_id: :attr:`~cozmo.objects.LightCube.cube_id`
        :param is_player: Whether the player or Cozmo played the wrong note.
        :return: None
        """
        self._sound.play()
        animation = Triggers.MemoryMatchPlayerLoseHand if is_player else Triggers.MemoryMatchCozmoLoseHand
        action = self._play_animation(animation, in_parallel=True)
        await self._note_cubes.flash_single_cube_red(cube_id)
        await action.wait_for_completed()